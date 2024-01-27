from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `user` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` DROP COLUMN `updated_at`;
        ALTER TABLE `user` DROP COLUMN `created_at`;"""
