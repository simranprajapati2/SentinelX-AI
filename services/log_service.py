from extensions import db
from models.activity_log import ActivityLog


def create_log(user_id, activity):

    log = ActivityLog(
        user_id=user_id,
        activity=activity
    )

    db.session.add(log)