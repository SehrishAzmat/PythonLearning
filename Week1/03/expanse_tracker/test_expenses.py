import json

import pytest
from models import Expense
from storage import load_expenses, save_expenses
from tracker import ExpenseTracker


def test_add_expense():
    tracker = ExpenseTracker()

    tracker.add_expense("Food", 500, "Lunch")

    assert len(tracker) == 1
    assert tracker.expenses[0].category == "Food"
    assert tracker.expenses[0].amount == 500
    assert tracker.expenses[0].description == "Lunch"


def test_add_multiple_expenses():
    tracker = ExpenseTracker()

    tracker.add_expense("Food", 500, "Lunch")
    tracker.add_expense("Transport", 200, "Bus")

    assert len(tracker) == 2


def test_calculate_total():
    tracker = ExpenseTracker()

    tracker.add_expense("Food", 500, "Lunch")
    tracker.add_expense("Transport", 200, "Bus")

    assert tracker.calculate_total() == 700


def test_calculate_total_with_no_expenses():
    tracker = ExpenseTracker()

    assert tracker.calculate_total() == 0


def test_calculate_total_with_decimal_amounts():
    tracker = ExpenseTracker()

    tracker.add_expense("Food", 100.50, "Lunch")
    tracker.add_expense("Transport", 50.25, "Bus")

    assert tracker.calculate_total() == pytest.approx(150.75)


def test_expense_string_representation():
    expense = Expense("Food", 500, "Lunch")

    assert str(expense) == "Food - 500.00 - Lunch"


def test_show_expenses(capsys):
    tracker = ExpenseTracker()
    tracker.add_expense("Food", 500, "Lunch")

    tracker.show_expenses()

    captured = capsys.readouterr()
    assert "Food - 500.00 - Lunch" in captured.out


def test_show_expenses_when_empty(capsys):
    tracker = ExpenseTracker()

    tracker.show_expenses()

    captured = capsys.readouterr()
    assert "No expenses found." in captured.out


def test_save_and_load_expenses(tmp_path, monkeypatch):
    test_file = tmp_path / "expenses.json"
    monkeypatch.setattr("storage.FILE_NAME", test_file)

    original = [
        Expense("Food", 500, "Lunch"),
        Expense("Transport", 200, "Bus"),
    ]

    save_expenses(original)
    loaded = load_expenses()

    assert len(loaded) == 2
    assert loaded[0] == original[0]
    assert loaded[1] == original[1]


def test_load_expenses_when_file_is_missing(tmp_path, monkeypatch):
    test_file = tmp_path / "missing.json"
    monkeypatch.setattr("storage.FILE_NAME", test_file)

    assert load_expenses() == []


def test_saved_json_contains_expense_details(tmp_path, monkeypatch):
    test_file = tmp_path / "expenses.json"
    monkeypatch.setattr("storage.FILE_NAME", test_file)

    save_expenses([Expense("Food", 500, "Lunch")])

    with test_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    assert data == [
        {
            "category": "Food",
            "amount": 500,
            "description": "Lunch",
        }
    ]


def test_load_expenses_rejects_non_list_json(tmp_path, monkeypatch):
    test_file = tmp_path / "expenses.json"
    test_file.write_text('{"category": "Food"}', encoding="utf-8")
    monkeypatch.setattr("storage.FILE_NAME", test_file)

    with pytest.raises(TypeError, match="expected a JSON list"):
        load_expenses()
