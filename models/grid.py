from decimal import Decimal
from typing import Optional, List

from sqlalchemy import Column, Text
from sqlmodel import SQLModel, Field, Relationship


class Grid(SQLModel, table=True):
    grid_id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(sa_column=Column(Text))
    voltage_level: Decimal = Field(max_digits=4, decimal_places=1)
    reduction_factor: Decimal = Field(max_digits=4, decimal_places=3)
    switch_off_time_touch_voltage: Decimal = Field(max_digits=5, decimal_places=3)
    switch_off_time_thermal: Decimal = Field(max_digits=5, decimal_places=3)

    # Relationships
    fault_current_touch_voltages: List["GridFaultCurrentTouchVoltage"] = Relationship(back_populates="grid")
    fault_current_thermals: List["GridFaultCurrentThermal"] = Relationship(back_populates="grid")


class GridFaultCurrentTouchVoltage(SQLModel, table=True):
    grid_fault_current_touch_voltage_id: Optional[int] = Field(primary_key=True, default=None)
    grid_id: Optional[int] = Field(foreign_key="grid.grid_id", default=None)
    frequency: Decimal = Field(max_digits=4, decimal_places=1)
    fault_current: Decimal = Field(max_digits=7, decimal_places=1)

    # Relationships
    grid: Optional[Grid] = Relationship(back_populates="fault_current_touch_voltages")


class GridFaultCurrentThermal(SQLModel, table=True):
    grid_fault_current_thermal_id: Optional[int] = Field(primary_key=True, default=None)
    grid_id: Optional[int] = Field(foreign_key="grid.grid_id", default=None)
    frequency: Decimal = Field(max_digits=4, decimal_places=1)
    fault_current: Decimal = Field(max_digits=7, decimal_places=1)

    # Relationships
    grid: Optional[Grid] = Relationship(back_populates="fault_current_thermals")
