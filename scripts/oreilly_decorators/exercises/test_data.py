TESTS = {
    "count_calls": "decorators_test.CountCallsTests",
    "four": "decorators_test.FourTests",
    "groot": "decorators_test.GrootTests",
    "jsonify": "decorators_test.JSONifyTests",
    "record_calls": "decorators_test.RecordCallsTests",
    "call_again": "functions_test.CallAgainTests",
    "call_later": "functions_test.CallLaterTests",
    "call_logger": "functions_test.CallLoggerTests",
    "call": "functions_test.CallTests",
    "exclude": "functions_test.ExcludeTests",
    "only_once": "functions_test.OnlyOnceTests",
    "is_ok": "initial_test.InitialTests",
    "at": "more_test.AtTests",
    "coalesce_all": "more_test.CoalesceAllTests",
    "lazy_repr": "more_test.LazyReprTests",
    "positional_only": "more_test.PositionalOnlyTests"
}

MODULES = {
    "decorators": [
        "count_calls",
        "jsonify",
        "groot",
        "four",
        "record_calls"
    ],
    "functions": [
        "call",
        "call_later",
        "exclude",
        "call_logger",
        "call_again",
        "only_once"
    ],
    "more": [
        "coalesce_all",
        "lazy_repr",
        "positional_only",
        "at"
    ],
    "initial": [
        "is_ok"
    ]
}
