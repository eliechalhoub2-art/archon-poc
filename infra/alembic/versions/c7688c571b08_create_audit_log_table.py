"""create audit_log table

Revision ID: c7688c571b08
Revises: 
Create Date: 2026-02-17 12:10:51.827181

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7688c571b08'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        "audit_log",
        sa.Column("audit_id", sa.String(length=36), primary_key=True),
        sa.Column("object_type", sa.String(length=100), nullable=False),
        sa.Column("object_id", sa.String(length=36), nullable=False),
        sa.Column("action", sa.String(length=50), nullable=False),
        sa.Column("actor_id", sa.String(length=36), nullable=False),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=True),
    )

    # Prevent UPDATE and DELETE (Append-Only enforcement)
    op.execute("""
        REVOKE UPDATE, DELETE ON TABLE audit_log FROM PUBLIC;
    """)

def downgrade():
    op.drop_table("audit_log")