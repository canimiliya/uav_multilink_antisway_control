from tools.verify_migration_parity import _compare_json, _compare_csv


def test_numeric_tolerance_and_boolean_exactness():
    failures = []
    stats = {"max_metric_diff": 0.0}
    _compare_json({"x": 1.0, "status": True}, {"x": 1.0 + 5e-10, "status": True}, "metrics", failures, stats)
    assert failures == []
    failures = []
    _compare_json({"status": True}, {"status": 1}, "metrics", failures, stats)
    assert failures


def test_runtime_metadata_is_ignored(tmp_path):
    failures = []
    stats = {"max_metric_diff": 0.0}
    _compare_json({"runtime_s": 1.0, "value": 2.0}, {"runtime_s": 99.0, "value": 2.0}, "metrics", failures, stats)
    assert failures == []


def test_csv_time_and_metadata_rules(tmp_path):
    left = tmp_path / "left.csv"
    right = tmp_path / "right.csv"
    text = "time,value,safe,process_id\n0.0,1.0,true,1\n"
    left.write_text(text, encoding="utf-8")
    right.write_text("time,value,safe,process_id\n0.0000000000005,1.0000000005,true,999\n", encoding="utf-8")
    failures = []
    stats = {"max_time_diff": 0.0, "max_state_diff": 0.0}
    result = _compare_csv(left, right, failures, stats)
    assert failures == []
    assert result["row_count_old"] == result["row_count_clean"] == 1
