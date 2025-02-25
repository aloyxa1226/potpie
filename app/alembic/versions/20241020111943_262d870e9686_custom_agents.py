"""custom_agents

Revision ID: 20241020111943_262d870e9686
Revises:
Create Date: 2024-10-20 11:19:43.653649

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "20241020111943_262d870e9686"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Add this line
branch_labels = ("custom_agents_microservice",)


def upgrade() -> None:
    if not op.get_bind().dialect.has_table(op.get_bind(), "custom_agents"):
        op.create_table(
            "custom_agents",
            sa.Column("id", sa.String(), nullable=False),
            sa.Column("user_id", sa.String(), nullable=True),
            sa.Column("role", sa.String(), nullable=True),
            sa.Column("goal", sa.String(), nullable=True),
            sa.Column("backstory", sa.String(), nullable=True),
            sa.Column("system_prompt", sa.String(), nullable=True),
            sa.Column("tasks", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
            sa.Column("deployment_url", sa.String(), nullable=True),
            sa.Column("deployment_status", sa.String(), nullable=False),
            sa.Column("created_at", sa.DateTime(), nullable=False),
            sa.Column("updated_at", sa.DateTime(), nullable=False),
            sa.PrimaryKeyConstraint("id"),
        )
        op.create_index(
            op.f("ix_custom_agents_id"), "custom_agents", ["id"], unique=False
        )
        op.create_index(
            op.f("ix_custom_agents_user_id"), "custom_agents", ["user_id"], unique=False
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_custom_agents_user_id"), table_name="custom_agents")
    op.drop_index(op.f("ix_custom_agents_id"), table_name="custom_agents")
    op.drop_table("custom_agents")
    # ### end Alembic commands ###
