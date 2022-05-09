"""import sqlachemy_utls to makofile

Revision ID: 1b945f69bfe5
Revises: bde1110b7f09
Create Date: 2022-05-09 13:16:37.514418

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '1b945f69bfe5'
down_revision = 'bde1110b7f09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_owner_id_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_post_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'users', ['owner_id'], ['id'], source_schema='core', referent_schema='core', ondelete='CASCADE')
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['id'], source_schema='core', referent_schema='core', ondelete='CASCADE')
    op.drop_constraint('posts_owner_id_fkey', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['owner_id'], ['id'], source_schema='core', referent_schema='core')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', schema='core', type_='foreignkey')
    op.create_foreign_key('posts_owner_id_fkey', 'posts', 'users', ['owner_id'], ['id'])
    op.drop_constraint(None, 'comments', schema='core', type_='foreignkey')
    op.drop_constraint(None, 'comments', schema='core', type_='foreignkey')
    op.create_foreign_key('comments_post_id_fkey', 'comments', 'posts', ['post_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('comments_owner_id_fkey', 'comments', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def render_item(type_, obj, autogen_context):
    """Apply custom rendering for selected items"""

    if type_ == "type" and isinstance(obj, sqlalchemy_utils.types.uuid.UUIDType):
        # Add import for this type
        autogen_context.imports.add("import sqlalchemy_utils")

        autogen_context.imports.add("import uuid")

        return "sqlalchemy_utils.types.uuid.UUIDType(), default=uuid.uuid4"

    # Default rendering for other objects
    return False