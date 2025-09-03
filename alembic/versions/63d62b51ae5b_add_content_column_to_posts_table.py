"""Add content column to posts table

Revision ID: 63d62b51ae5b
Revises: 291164184221
Create Date: 2025-09-02 21:39:31.912592

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63d62b51ae5b'
down_revision: Union[str, Sequence[str], None] = '291164184221'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
