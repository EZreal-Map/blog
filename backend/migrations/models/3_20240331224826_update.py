from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `time` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `start_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `end_time` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `time`;"""
