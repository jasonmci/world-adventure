# tests/test_hex_cell.py

import pytest
from src.classes.hex_cell import HexCell

def test_hex_cell_initialization():
    cell = HexCell("grass", False)

    assert cell.terrain == "grass"
    assert cell.has_object == False

def test_hex_cell_change_terrain():
    cell = HexCell("grass", False)

    cell.terrain = "water"
    assert cell.terrain == "water"

def test_hex_cell_object_presence():
    cell = HexCell("grass", False)

    cell.has_object = True
    assert cell.has_object == True
