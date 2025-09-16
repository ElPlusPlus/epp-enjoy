from enum import Enum
from typing import Union

class ModbusAccess(Enum):
    RO = "RO"
    RW = "RW" 
    WO = "WO"

class ModbusType(Enum):
   """Types of data used in Modbus registers"""
   STRING = "String"
   U16 = "U16"        
   E16 = "E16"          
   U32 = "U32"        
   S16 = "S16"      
   S32 = "S32"          
   B16 = "B16"         
   I16 = "I16"
   I32 = "I32"

class ModbusUnit(Enum):
   """Units of measurement for Modbus register values"""
   NONE = ""
   WATT = "W"
   KILO_WATT = "kW"
   VOLT = "V"
   AMPERE = "A"
   HERTZ = "Hz"
   CELSIUS = "℃"
   KWH = "kWh"
   HOUR = "H"
   SECOND = "s"
   VA = "VA"
   VAR = "Var"
   PERCENTAGE = "%"
   KOHM = "kΩ"
   WH = "WH"
   MILLISECOND = "MILLISECOND"

class ModbusRegister():
   """Definition of a Modbus register including its address range, type, unit and function code"""
   def __init__(self, 
                 register: int,
                 count: int, 
                 function_code: int,
                 modbus_type: ModbusType,
                 modbus_unit: ModbusUnit,
                 access: ModbusAccess = ModbusAccess.RO,
                 gain: float = 1.0
                 ):
        self.register: int = register
        self.count: int = count
        self.function_code: int = function_code 
        self.modbus_type: ModbusType = modbus_type
        self.modbus_unit: ModbusUnit = modbus_unit
        self.access: ModbusAccess = access
        self.gain:float = gain

class Result:
    """Definition of a Returned Modbus register including its address range, type, unit and function code"""
    def __init__(self,
            name: str,
            value: Union[str, int] | None,
            modbus_type: ModbusType,
            register: int,
            count: int, 
            function_code: int,
            modbus_unit: ModbusUnit):
        self.name = name
        self.register: int = register
        self.count: int = count
        self.modbus_type: ModbusType = modbus_type
        self.function_code: int = function_code 
        self.value: Union[str, int] = value
        self.modbus_unit: ModbusUnit = modbus_unit

    def __str__(self):
        return ((self.name or "Name NaN")
                + " ("
                + str(self.register or "")
                + ", "
                + str(self.function_code or "")
                + ", "
                + str(self.count or "")
                + ", "
                + (self.modbus_type.value if self.modbus_type is not None else "")
                + "): "
                + str(self.value or "")
                + " "
                + (self.modbus_unit.value if self.modbus_unit is not None else ""))