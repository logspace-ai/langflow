"""Adds Credential table

Revision ID: c1c8e217a069
Revises: 7d2162acc8b2
Create Date: 2023-11-24 10:45:38.465302

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision: str = "2ac71eb9c3ae"
down_revision: Union[str, None] = "7d2162acc8b2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)  # type: ignore
    tables = inspector.get_table_names()
    try:
        if "credential" not in tables:
            op.create_table(
                "credential",
                sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
                sa.Column("value", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
                sa.Column(
                    "provider", sqlmodel.sql.sqltypes.AutoString(), nullable=True
                ),
                sa.Column("user_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
                sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
                sa.Column("created_at", sqlmodel.sql.sqltypes.DateTime(), nullable=False),
                sa.Column("updated_at", sa.DateTime(), nullable=True),
                sa.PrimaryKeyConstraint("id"),
            )
    except Exception as e:
        print(e)

        pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.drop_table("credential")
    except Exception as e:
        print(e)
        pass
    # ### end Alembic commands ###
