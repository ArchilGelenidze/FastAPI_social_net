"""Add user table

Revision ID: 52b947c17085
Revises: 63d62b51ae5b
Create Date: 2025-09-03 18:19:19.933391

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52b947c17085'
down_revision: Union[str, Sequence[str], None] = '63d62b51ae5b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False,),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
