"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    ${upgrades if upgrades else "pass"}


def downgrade():
    ${downgrades if downgrades else "pass"}


def render_item(type_, obj, autogen_context):
    """Apply custom rendering for selected items"""

    if type_ == "type" and isinstance(obj, sqlalchemy_utils.types.uuid.UUIDType):
        # Add import for this type
        autogen_context.imports.add("import sqlalchemy_utils")

        autogen_context.imports.add("import uuid")

        return "sqlalchemy_utils.types.uuid.UUIDType(), default=uuid.uuid4"

    # Default rendering for other objects
    return False