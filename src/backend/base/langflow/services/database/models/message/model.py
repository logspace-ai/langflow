from datetime import datetime, timezone
from typing import TYPE_CHECKING, List, Optional
from uuid import UUID, uuid4

from sqlmodel import JSON, Column, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from langflow.schema.message import Message
    from langflow.services.database.models.flow.model import Flow


class MessageBase(SQLModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    sender: str
    sender_name: str
    session_id: str
    text: str
    files: list[str] = Field(default_factory=list)

    @classmethod
    def from_message(cls, message: "Message", flow_id: str | None = None):
        # first check if the record has all the required fields
        if message.text is None or not message.sender or not message.sender_name:
            raise ValueError("The message does not have the required fields (text, sender, sender_name).")
        return cls(
            sender=message.sender,
            sender_name=message.sender_name,
            text=message.text,
            session_id=message.session_id,
            files=message.files or [],
            timestamp=message.timestamp,
            flow_id=flow_id,
        )


class MessageTable(MessageBase, table=True):
    __tablename__ = "message"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    flow_id: Optional[UUID] = Field(default=None, foreign_key="flow.id")
    flow: "Flow" = Relationship(back_populates="messages")
    files: List[str] = Field(sa_column=Column(JSON))

    # Needed for Column(JSON)
    class Config:
        arbitrary_types_allowed = True


class MessageRead(MessageBase):
    id: UUID
    flow_id: Optional[UUID] = Field()


class MessageCreate(MessageBase):
    pass


class MessageUpdate(SQLModel):
    text: Optional[str] = None
    sender: Optional[str] = None
    sender_name: Optional[str] = None
    session_id: Optional[str] = None
    files: Optional[list[str]] = None