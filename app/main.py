from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models import AuditLog

app = FastAPI(title="ARCHON PoC v0.1")

@app.post("/ping")
def ping(db: Session = Depends(get_db)):
    event = AuditLog(
        actor="system",
        action="PING",
        object_type="SYSTEM",
        object_id="ping",
        payload={"message": "hello", "locked_scope": True},
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return {"ok": True, "audit_id": event.id}
