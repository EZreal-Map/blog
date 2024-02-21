from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` ADD UNIQUE INDEX `uid_user_email_1b4f1c` (`email`);
        ALTER TABLE `user` ADD UNIQUE INDEX `uid_user_nicknam_579938` (`nickname`);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` DROP INDEX `idx_user_nicknam_579938`;
        ALTER TABLE `user` DROP INDEX `idx_user_email_1b4f1c`;"""
