import jodel_api
from bottle import Bottle, run, HTTPError, request, response
import pickledb
import json

from .conf import (
    JODEL_DB_PATH,
    JODEL_DEFAULT_LAT, JODEL_DEFAULT_LNG, DEFAULT_CITY,
    JODEL_ACCESS_TOKEN, JODEL_DEVICE_UID, JODEL_REFRESH_TOKEN,
    JODEL_DISTRINCT_ID, JODEL_EXPIRATION_DATE
)

hr = Bottle()
db = pickledb.load(JODEL_DB_PATH, auto_dump=True)

@hr.route("/poll/<our_id:re:[a-z0-9:]+>")
def poll(our_id):
    jodel = jodel_api.JodelAccount(lat=JODEL_DEFAULT_LAT,
                                   lng=JODEL_DEFAULT_LNG,
                                   city=DEFAULT_CITY,
                                   update_location=False,
                                   access_token=JODEL_ACCESS_TOKEN,
                                   device_uid=JODEL_DEVICE_UID,
                                   refresh_token=JODEL_REFRESH_TOKEN,
                                   distinct_id=JODEL_DISTRINCT_ID,
                                   expiration_date=JODEL_EXPIRATION_DATE)
    post_id = db.get(our_id)
    if post_id:
        r = jodel.get_post_details(post_id)
        if r[0] != 200:
            return HTTPError(500, "Ausgejodelt.")
        post_details = r[1]

        response.content_type = "application/json"
        return json.dumps({k: v for k, v in post_details.items() if k in [
            "message", "poll_options", "poll_votes",
            "created_at", "updated_at",
            "votable"
        ]}, ensure_ascii=False)
    elif set(request.params.keys()) == set(["city", "lat", "lng",
                                            "channel", "message",
                                            "poll_option"]):
        r = jodel.set_location(
            float(request.params.lat),
            float(request.params.lng),
            request.params.city
        )
        if r[0] != 204:
            return HTTPError(500, "Ausgejodelt.")
        r = jodel.create_post(
            channel=request.params.channel,
            message=request.params.message,
            poll_options=request.params.getall("poll_option")
        )
        if r[0] != 200:
            return HTTPError(500, "Ausgejodelt.")
        if r[1] == {}:
            return HTTPError(500, "Ausgejodelt.")
        post_details = r[1]["post"]
        db.set(our_id, post_details["post_id"])

        response.content_type = "application/json"
        return json.dumps({k: v for k, v in post_details.items() if k in [
            "message", "channel", "poll_options", "poll_votes",
            "created_at", "updated_at",
            "votable"
        ]}, ensure_ascii=False)
    else:
        return HTTPError(404, "Poll not found")


@hr.route("/poll/<our_id:re:[a-z0-9:]+>/replies")
def poll_replies(our_id):
    jodel = jodel_api.JodelAccount(lat=JODEL_DEFAULT_LAT,
                                   lng=JODEL_DEFAULT_LNG,
                                   city=DEFAULT_CITY,
                                   update_location=False,
                                   access_token=JODEL_ACCESS_TOKEN,
                                   device_uid=JODEL_DEVICE_UID,
                                   refresh_token=JODEL_REFRESH_TOKEN,
                                   distinct_id=JODEL_DISTRINCT_ID,
                                   expiration_date=JODEL_EXPIRATION_DATE)
    post_id = db.get(our_id)
    if post_id:
        r = jodel.get_post_details_v3(post_id)
        if r[0] != 200:
            return HTTPError(500, "Ausgejodelt.")
        replies = r[1]["replies"]

        response.content_type = "application/json"
        return json.dumps([{k: v for k, v in reply.items() if k in [
                "message", "poll_vote",
                "created_at", "updated_at",
                "distance"
            ]} for reply in replies if reply["post_type"] != "automatic_reply"],
            ensure_ascii=False
        )
    else:
        return HTTPError(404, "Poll not found")
