import numpy as np
from pandas import Timestamp

expected_performance = 0.985296
expected_outperformance = -0.030969

expected_optimization_results = ({"ma": 1.0}, 0.999557)

expected_results = {
    1: [
        {
            "close_time": Timestamp("2023-09-01 14:14:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 0,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
            "returns": 0.0,
            "SMA": 55388.96,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.0,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratios": 0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:19:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 0,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
            "returns": 0.0,
            "SMA": 55388.96,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.0,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratios": 0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:29:59.999000+0000", tz="UTC"),
            "open": 55388.95,
            "high": 55569.95,
            "low": 55388.95,
            "close": 55552.4,
            "volume": 149.363426,
            "quote_volume": 8288967.03877351,
            "trades": 1,
            "taker_buy_asset_volume": 82.67909,
            "taker_buy_quote_volume": 4588065.23181743,
            "returns": 0.002946423556387118,
            "SMA": 55429.82000000001,
            "side": -1,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.002950768528602,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratios": 0.004002528142238611,
        },
        {
            "close_time": Timestamp("2023-09-01 14:34:59.999000+0000", tz="UTC"),
            "open": 55550.89,
            "high": 56087.68,
            "low": 55550.89,
            "close": 55932.48,
            "volume": 692.924319,
            "quote_volume": 38726480.58078431,
            "trades": 0,
            "taker_buy_asset_volume": 411.223017,
            "taker_buy_quote_volume": 22979821.33981915,
            "returns": 0.006818529518377586,
            "SMA": 55565.7,
            "side": -1,
            "strategy_returns": -0.006818529518377586,
            "strategy_returns_tc": -0.006818529518377586,
            "accumulated_returns": 1.0098127857970252,
            "accumulated_strategy_returns": 0.993204663909056,
            "accumulated_strategy_returns_tc": 0.993204663909056,
            "margin_ratios": 0.004077834681277391,
        },
        {
            "close_time": Timestamp("2023-09-01 14:39:59.999000+0000", tz="UTC"),
            "open": 55932.48,
            "high": 56333.0,
            "low": 55932.48,
            "close": 56264.93,
            "volume": 603.660118,
            "quote_volume": 33896505.6971466,
            "trades": 0,
            "taker_buy_asset_volume": 356.915883,
            "taker_buy_quote_volume": 20037884.70780964,
            "returns": 0.005926179097336494,
            "SMA": 55784.692500000005,
            "side": -1,
            "strategy_returns": -0.005926179097336494,
            "strategy_returns_tc": -0.005926179097336494,
            "accumulated_returns": 1.0158148844101784,
            "accumulated_strategy_returns": 0.9873361612642192,
            "accumulated_strategy_returns_tc": 0.9873361612642192,
            "margin_ratios": 0.004114014876268444,
        },
        {
            "close_time": Timestamp("2023-09-01 14:44:59.999000+0000", tz="UTC"),
            "open": 56260.11,
            "high": 56317.43,
            "low": 56118.31,
            "close": 56168.82,
            "volume": 370.500359,
            "quote_volume": 20822485.25288953,
            "trades": 0,
            "taker_buy_asset_volume": 178.075904,
            "taker_buy_quote_volume": 10007121.78892216,
            "returns": -0.00170962942015996,
            "SMA": 55979.6575,
            "side": -1,
            "strategy_returns": 0.00170962942015996,
            "strategy_returns_tc": 0.00170962942015996,
            "accumulated_returns": 1.0140797010812264,
            "accumulated_strategy_returns": 0.9890255839449716,
            "accumulated_strategy_returns_tc": 0.9890255839449716,
            "margin_ratios": 0.004111708957739713,
        },
        {
            "close_time": Timestamp("2023-09-01 14:49:59.999000+0000", tz="UTC"),
            "open": 56168.82,
            "high": 56269.99,
            "low": 56080.96,
            "close": 56191.11,
            "volume": 324.51432,
            "quote_volume": 18225087.41727558,
            "trades": 0,
            "taker_buy_asset_volume": 145.064381,
            "taker_buy_quote_volume": 8146012.47892439,
            "returns": 0.0003967606653441501,
            "SMA": 56139.335,
            "side": -1,
            "strategy_returns": -0.0003967606653441501,
            "strategy_returns_tc": -0.0003967606653441501,
            "accumulated_returns": 1.0144821278464156,
            "accumulated_strategy_returns": 0.9886332553316708,
            "accumulated_strategy_returns_tc": 0.9886332553316708,
            "margin_ratios": 0.004104691162420367,
        },
        {
            "close_time": Timestamp("2023-09-01 14:54:59.999000+0000", tz="UTC"),
            "open": 56191.11,
            "high": 56200.0,
            "low": 56107.98,
            "close": 56145.0,
            "volume": 254.091606,
            "quote_volume": 14265787.89818125,
            "trades": 2,
            "taker_buy_asset_volume": 134.1124,
            "taker_buy_quote_volume": 7529521.30623853,
            "returns": -0.0008209293091875578,
            "SMA": 56192.465000000004,
            "side": 1,
            "strategy_returns": 0.0008209293091875578,
            "strategy_returns_tc": 0.0008209293091875578,
            "accumulated_returns": 1.0136496514828948,
            "accumulated_strategy_returns": 0.9894451865704871,
            "accumulated_strategy_returns_tc": 0.9894451865704871,
            "margin_ratios": 0.004,
        },
        {
            "close_time": Timestamp("2023-09-01 14:59:59.999000+0000", tz="UTC"),
            "open": 56145.0,
            "high": 56211.7,
            "low": 56106.97,
            "close": 56182.11,
            "volume": 270.145731,
            "quote_volume": 15171017.18758856,
            "trades": 2,
            "taker_buy_asset_volume": 168.231118,
            "taker_buy_quote_volume": 9447425.0774598,
            "returns": 0.0006607487960858385,
            "SMA": 56171.759999999995,
            "side": -1,
            "strategy_returns": 0.0006607487960858385,
            "strategy_returns_tc": 0.0006607487960858385,
            "accumulated_returns": 1.014319640592638,
            "accumulated_strategy_returns": 0.9900991773243144,
            "accumulated_strategy_returns_tc": 0.9900991773243144,
            "margin_ratios": 0.004004215661202739,
        },
        {
            "close_time": Timestamp("2023-09-01 15:04:59.999000+0000", tz="UTC"),
            "open": 56182.12,
            "high": 56299.78,
            "low": 56172.09,
            "close": 56289.89,
            "volume": 298.797415,
            "quote_volume": 16804824.55255641,
            "trades": 1,
            "taker_buy_asset_volume": 139.83665,
            "taker_buy_quote_volume": 7864202.02549528,
            "returns": 0.0019165664875115606,
            "SMA": 56202.027500000004,
            "side": 0,
            "strategy_returns": -0.0019165664875115606,
            "strategy_returns_tc": -0.0019165664875115606,
            "accumulated_returns": 1.016265515727322,
            "accumulated_strategy_returns": 0.9882034036901499,
            "accumulated_strategy_returns_tc": 0.9882034036901499,
            "margin_ratios": 0.004008377755837223,
        },
    ],
    10: [
        {
            "close_time": Timestamp("2023-09-01 14:14:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 0,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
            "returns": 0.0,
            "SMA": 55388.96,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.0,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratios": 0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:19:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 0,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
            "returns": 0.0,
            "SMA": 55388.96,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.0,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratios": 0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:29:59.999000+0000", tz="UTC"),
            "open": 55388.95,
            "high": 55569.95,
            "low": 55388.95,
            "close": 55552.4,
            "volume": 149.363426,
            "quote_volume": 8288967.03877351,
            "trades": 1,
            "taker_buy_asset_volume": 82.67909,
            "taker_buy_quote_volume": 4588065.23181743,
            "returns": 0.002946423556387118,
            "SMA": 55429.82000000001,
            "side": -1,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.002950768528602,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratios": 0.04013944442538307,
        },
        {
            "close_time": Timestamp("2023-09-01 14:34:59.999000+0000", tz="UTC"),
            "open": 55550.89,
            "high": 56087.68,
            "low": 55550.89,
            "close": 55932.48,
            "volume": 692.924319,
            "quote_volume": 38726480.58078431,
            "trades": 0,
            "taker_buy_asset_volume": 411.223017,
            "taker_buy_quote_volume": 22979821.33981915,
            "returns": 0.006818529518377586,
            "SMA": 55565.7,
            "side": -1,
            "strategy_returns": -0.006818529518377586,
            "strategy_returns_tc": -0.006818529518377586,
            "accumulated_returns": 1.0098127857970252,
            "accumulated_strategy_returns": 0.993204663909056,
            "accumulated_strategy_returns_tc": 0.993204663909056,
            "margin_ratios": 0.04469173459549476,
        },
        {
            "close_time": Timestamp("2023-09-01 14:39:59.999000+0000", tz="UTC"),
            "open": 55932.48,
            "high": 56333.0,
            "low": 55932.48,
            "close": 56264.93,
            "volume": 603.660118,
            "quote_volume": 33896505.6971466,
            "trades": 0,
            "taker_buy_asset_volume": 356.915883,
            "taker_buy_quote_volume": 20037884.70780964,
            "returns": 0.005926179097336494,
            "SMA": 55784.692500000005,
            "side": -1,
            "strategy_returns": -0.005926179097336494,
            "strategy_returns_tc": -0.005926179097336494,
            "accumulated_returns": 1.0158148844101784,
            "accumulated_strategy_returns": 0.9873361612642192,
            "accumulated_strategy_returns_tc": 0.9873361612642192,
            "margin_ratios": 0.04719350568838694,
        },
        {
            "close_time": Timestamp("2023-09-01 14:44:59.999000+0000", tz="UTC"),
            "open": 56260.11,
            "high": 56317.43,
            "low": 56118.31,
            "close": 56168.82,
            "volume": 370.500359,
            "quote_volume": 20822485.25288953,
            "trades": 0,
            "taker_buy_asset_volume": 178.075904,
            "taker_buy_quote_volume": 10007121.78892216,
            "returns": -0.00170962942015996,
            "SMA": 55979.6575,
            "side": -1,
            "strategy_returns": 0.00170962942015996,
            "strategy_returns_tc": 0.00170962942015996,
            "accumulated_returns": 1.0140797010812264,
            "accumulated_strategy_returns": 0.9890255839449716,
            "accumulated_strategy_returns_tc": 0.9890255839449716,
            "margin_ratios": 0.047027107371075544,
        },
        {
            "close_time": Timestamp("2023-09-01 14:49:59.999000+0000", tz="UTC"),
            "open": 56168.82,
            "high": 56269.99,
            "low": 56080.96,
            "close": 56191.11,
            "volume": 324.51432,
            "quote_volume": 18225087.41727558,
            "trades": 0,
            "taker_buy_asset_volume": 145.064381,
            "taker_buy_quote_volume": 8146012.47892439,
            "returns": 0.0003967606653441501,
            "SMA": 56139.335,
            "side": -1,
            "strategy_returns": -0.0003967606653441501,
            "strategy_returns_tc": -0.0003967606653441501,
            "accumulated_returns": 1.0144821278464156,
            "accumulated_strategy_returns": 0.9886332553316708,
            "accumulated_strategy_returns_tc": 0.9886332553316708,
            "margin_ratios": 0.04652671441712397,
        },
        {
            "close_time": Timestamp("2023-09-01 14:54:59.999000+0000", tz="UTC"),
            "open": 56191.11,
            "high": 56200.0,
            "low": 56107.98,
            "close": 56145.0,
            "volume": 254.091606,
            "quote_volume": 14265787.89818125,
            "trades": 2,
            "taker_buy_asset_volume": 134.1124,
            "taker_buy_quote_volume": 7529521.30623853,
            "returns": -0.0008209293091875578,
            "SMA": 56192.465000000004,
            "side": 1,
            "strategy_returns": 0.0008209293091875578,
            "strategy_returns_tc": 0.0008209293091875578,
            "accumulated_returns": 1.0136496514828948,
            "accumulated_strategy_returns": 0.9894451865704871,
            "accumulated_strategy_returns_tc": 0.9894451865704871,
            "margin_ratios": 0.04023894662105466,
        },
        {
            "close_time": Timestamp("2023-09-01 14:59:59.999000+0000", tz="UTC"),
            "open": 56145.0,
            "high": 56211.7,
            "low": 56106.97,
            "close": 56182.11,
            "volume": 270.145731,
            "quote_volume": 15171017.18758856,
            "trades": 2,
            "taker_buy_asset_volume": 168.231118,
            "taker_buy_quote_volume": 9447425.0774598,
            "returns": 0.0006607487960858385,
            "SMA": 56171.759999999995,
            "side": -1,
            "strategy_returns": 0.0006607487960858385,
            "strategy_returns_tc": 0.0006607487960858385,
            "accumulated_returns": 1.014319640592638,
            "accumulated_strategy_returns": 0.9900991773243144,
            "accumulated_strategy_returns_tc": 0.9900991773243144,
            "margin_ratios": 0.040232966236214605,
        },
        {
            "close_time": Timestamp("2023-09-01 15:04:59.999000+0000", tz="UTC"),
            "open": 56182.12,
            "high": 56299.78,
            "low": 56172.09,
            "close": 56289.89,
            "volume": 298.797415,
            "quote_volume": 16804824.55255641,
            "trades": 1,
            "taker_buy_asset_volume": 139.83665,
            "taker_buy_quote_volume": 7864202.02549528,
            "returns": 0.0019165664875115606,
            "SMA": 56202.027500000004,
            "side": 0,
            "strategy_returns": -0.0019165664875115606,
            "strategy_returns_tc": -0.0019165664875115606,
            "accumulated_returns": 1.016265515727322,
            "accumulated_strategy_returns": 0.9882034036901499,
            "accumulated_strategy_returns_tc": 0.9882034036901499,
            "margin_ratios": 0.04008377755837223,
        },
    ],
}
