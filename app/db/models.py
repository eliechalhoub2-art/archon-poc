from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DateTime, JSON, func

class Base(DeclarativeBase):
    pass

class AuditLog(Base):
    __tablename__ = "audit_log"

    id: Mapped[int] = mapped_column(primary_key=True)
    actor: Mapped[str] = mapped_column(String(64), nullable=False)   # في PoC: "system" أو "elie"
    action: Mapped[str] = mapped_column(String(64), nullable=False)  # مثال: "PING"
    object_type: Mapped[str] = mapped_column(String(64), nullable=False)  # مثال: "SYSTEM"
    object_id: Mapped[str] = mapped_column(String(64), nullable=False)    # مثال: "ping"
    payload: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)

    created_at: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
