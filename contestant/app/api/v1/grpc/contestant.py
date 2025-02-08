import grpc
from sqlalchemy.orm import Session

from . import contestant_pb2
from . import contestant_pb2_grpc
from app.core.db import SessionLocal
from app.models.contestant import Contestant


class ContestantService(contestant_pb2_grpc.ContestantServiceServicer):
    def GetContestant(self, request, context):
        db: Session = SessionLocal()

        contestant = db.query(Contestant).filter(Contestant.id ==
                                                 request.id).first()

        db.close()

        if not contestant:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Contestant not found")
            return contestant_pb2.ContestantResponse()

        return contestant_pb2.ContestantResponse(
            id=contestant.id,
            username=contestant.username,
            age=contestant.age
        )
