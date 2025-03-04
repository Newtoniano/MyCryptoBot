import logging
import os

from apscheduler.schedulers.background import BackgroundScheduler

from execution.service.cron_jobs.save_pipelines_snapshot import save_pipelines_snapshot
from shared.utils.decorators import handle_db_connection_error


@handle_db_connection_error
def start_background_scheduler(binance_trader_objects, config_vars):

    logging.info('Starting scheduler.')

    interval_between_snapshots = os.getenv('SNAPSHOTS_INTERVAL', config_vars.app_snapshot_interval_seconds)

    # Create an instance of scheduler and add function.
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        lambda: save_pipelines_snapshot(binance_trader_objects),
        "interval",
        seconds=int(interval_between_snapshots)
    )

    scheduler.start()
