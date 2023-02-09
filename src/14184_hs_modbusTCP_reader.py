# coding: utf-8

import time
import pymodbus  # To not delete this module reference!!
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ConnectionException

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Hs_modbusTCP_reader14184(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "hs_modbusTCP_reader14184")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE,())
        self.PIN_I_SWITCH=1
        self.PIN_I_FETCH_INTERVAL=2
        self.PIN_I_MAN_TRIGGER=3
        self.PIN_I_MODBUS_SLAVE_IP=4
        self.PIN_I_PORT=5
        self.PIN_I_SLAVE_ID=6
        self.PIN_I_OPTIONS=7
        self.PIN_I_MODBUS_WORDORDER=8
        self.PIN_I_MODBUS_BYTEORDER=9
        self.PIN_I_REG_OFFSET=10
        self.PIN_I_ENABLE_DEBUG=11
        self.PIN_I_REGISTER1=12
        self.PIN_I_REG1_REGTYP=13
        self.PIN_I_REG1_DATATYPE=14
        self.PIN_I_REG1_MULTI_LEN=15
        self.PIN_I_REGISTER2=16
        self.PIN_I_REG2_REGTYP=17
        self.PIN_I_REG2_DATATYPE=18
        self.PIN_I_REG2_MULTI_LEN=19
        self.PIN_I_REGISTER3=20
        self.PIN_I_REG3_REGTYP=21
        self.PIN_I_REG3_DATATYPE=22
        self.PIN_I_REG3_MULTI_LEN=23
        self.PIN_I_REGISTER4=24
        self.PIN_I_REG4_REGTYP=25
        self.PIN_I_REG4_DATATYPE=26
        self.PIN_I_REG4_MULTI_LEN=27
        self.PIN_I_REGISTER5=28
        self.PIN_I_REG5_REGTYP=29
        self.PIN_I_REG5_DATATYPE=30
        self.PIN_I_REG5_MULTI_LEN=31
        self.PIN_I_REGISTER6=32
        self.PIN_I_REG6_REGTYP=33
        self.PIN_I_REG6_DATATYPE=34
        self.PIN_I_REG6_MULTI_LEN=35
        self.PIN_I_REGISTER7=36
        self.PIN_I_REG7_REGTYP=37
        self.PIN_I_REG7_DATATYPE=38
        self.PIN_I_REG7_MULTI_LEN=39
        self.PIN_I_REGISTER8=40
        self.PIN_I_REG8_REGTYP=41
        self.PIN_I_REG8_DATATYPE=42
        self.PIN_I_REG8_MULTI_LEN=43
        self.PIN_O_FETCH_OK=1
        self.PIN_O_REG1_VAL_NUM=2
        self.PIN_O_REG1_VAL_STR=3
        self.PIN_O_REG2_VAL_NUM=4
        self.PIN_O_REG2_VAL_STR=5
        self.PIN_O_REG3_VAL_NUM=6
        self.PIN_O_REG3_VAL_STR=7
        self.PIN_O_REG4_VAL_NUM=8
        self.PIN_O_REG4_VAL_STR=9
        self.PIN_O_REG5_VAL_NUM=10
        self.PIN_O_REG5_VAL_STR=11
        self.PIN_O_REG6_VAL_NUM=12
        self.PIN_O_REG6_VAL_STR=13
        self.PIN_O_REG7_VAL_NUM=14
        self.PIN_O_REG7_VAL_STR=15
        self.PIN_O_REG8_VAL_NUM=16
        self.PIN_O_REG8_VAL_STR=17
        self.FRAMEWORK._run_in_context_thread(self.on_init)

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

        self.DEBUG = None
        self.interval = None
        self.client = None
        self.data_types = {
            'int8': {'size': 1, 'numeric': True, 'method': 'decode_8bit_int'},
            'uint8': {'size': 1, 'numeric': True, 'method': 'decode_8bit_uint'},
            'int16': {'size': 1, 'numeric': True, 'method': 'decode_16bit_int'},
            'uint16': {'size': 1, 'numeric': True, 'method': 'decode_16bit_uint'},
            'int32': {'size': 2, 'numeric': True, 'method': 'decode_32bit_int'},
            'uint32': {'size': 2, 'numeric': True, 'method': 'decode_32bit_uint'},
            'int64': {'size': 4, 'numeric': True, 'method': 'decode_64bit_int'},
            'uint64': {'size': 4, 'numeric': True, 'method': 'decode_64bit_uint'},
            # 'float16': {'size': 2, 'numeric': True, 'method': 'decode_16bit_float'}, Doesn't work with python 2
            'float32': {'size': 2, 'numeric': True, 'method': 'decode_32bit_float'},
            'float64': {'size': 4, 'numeric': True, 'method': 'decode_64bit_float'},
            'string': {'size': -1, 'numeric': False, 'method': 'decode_string'}
        }
        self.options = {
            'KeepAlive', 'Sleep100ms', 'Sleep500ms', 'ReconnectAfterEachRead'
        }

    def on_interval(self):

        ip_address = str(self._get_input_value(self.PIN_I_MODBUS_SLAVE_IP))
        port = int(self._get_input_value(self.PIN_I_PORT))
        unit_id = int(self._get_input_value(self.PIN_I_SLAVE_ID))

        try:
            self.log_debug("Conn IP:Port (UnitID)", ip_address + ":" + str(port) + " (" + str(unit_id) + ") ")
            if self.client is None:
                self.client = ModbusTcpClient(ip_address, port, timeout=15, retry_on_empty=True, retry_on_invalid=True,
                    reset_socket=False)  # reset_socket=true caused some issues with devices

            self.fetch_register(1, self.PIN_I_REGISTER1, self.PIN_I_REG1_REGTYP, self.PIN_I_REG1_DATATYPE,
                                self.PIN_I_REG1_MULTI_LEN, self.PIN_O_REG1_VAL_NUM, self.PIN_O_REG1_VAL_STR, unit_id)
            self.fetch_register(2, self.PIN_I_REGISTER2, self.PIN_I_REG2_REGTYP, self.PIN_I_REG2_DATATYPE,
                                self.PIN_I_REG2_MULTI_LEN, self.PIN_O_REG2_VAL_NUM, self.PIN_O_REG2_VAL_STR, unit_id)
            self.fetch_register(3, self.PIN_I_REGISTER3, self.PIN_I_REG3_REGTYP, self.PIN_I_REG3_DATATYPE,
                                self.PIN_I_REG3_MULTI_LEN, self.PIN_O_REG3_VAL_NUM, self.PIN_O_REG3_VAL_STR, unit_id)
            self.fetch_register(4, self.PIN_I_REGISTER4, self.PIN_I_REG4_REGTYP, self.PIN_I_REG4_DATATYPE,
                                self.PIN_I_REG4_MULTI_LEN, self.PIN_O_REG4_VAL_NUM, self.PIN_O_REG4_VAL_STR, unit_id)
            self.fetch_register(5, self.PIN_I_REGISTER5, self.PIN_I_REG5_REGTYP, self.PIN_I_REG5_DATATYPE,
                                self.PIN_I_REG5_MULTI_LEN, self.PIN_O_REG5_VAL_NUM, self.PIN_O_REG5_VAL_STR, unit_id)
            self.fetch_register(6, self.PIN_I_REGISTER6, self.PIN_I_REG6_REGTYP, self.PIN_I_REG6_DATATYPE,
                                self.PIN_I_REG6_MULTI_LEN, self.PIN_O_REG6_VAL_NUM, self.PIN_O_REG6_VAL_STR, unit_id)
            self.fetch_register(7, self.PIN_I_REGISTER7, self.PIN_I_REG7_REGTYP, self.PIN_I_REG7_DATATYPE,
                                self.PIN_I_REG7_MULTI_LEN, self.PIN_O_REG7_VAL_NUM, self.PIN_O_REG7_VAL_STR, unit_id)
            self.fetch_register(8, self.PIN_I_REGISTER8, self.PIN_I_REG8_REGTYP, self.PIN_I_REG8_DATATYPE,
                                self.PIN_I_REG8_MULTI_LEN, self.PIN_O_REG8_VAL_NUM, self.PIN_O_REG8_VAL_STR, unit_id)
        except ConnectionException as con_err:
            self.log_debug("Last exception msg logged", "Message: " + str(con_err))
            self.LOGGER.warning("Unable to read modbus register: " + str(con_err))
            self.client = None  # Restart with fresh client!
        except Exception as err:
            self.log_debug("Last perm exception msg logged", "Message: " + str(err))
            self.LOGGER.error("Unable to read modbus register. Perm error: " + str(err))
            if self.client:
                self.client.close()
                self.client = None  # Restart with fresh client!
            # Throw exception only if in debug mode
            if bool(self._get_input_value(self.PIN_I_ENABLE_DEBUG)):
                raise
        finally:
            if self.client and not self.is_option_set('KeepAlive'):
                self.client.close()
                # Let's drop the client without keepalive to start with new client. Had an issue at 4.2.2023
                self.client = None
        # No exception raised and maybe connection closed: Lets notify the next module
        self._set_output_value(self.PIN_O_FETCH_OK, 1)

    def fetch_register(self, input_num, input_addr_id, input_reg_read_type, input_reg_datatype,
                       multiplier_fetchsize_input, pin_output_num_id, pin_output_str_id, unit_id):

        self.client.connect()

        try:
            # Get register address and apply offset
            register_addr = int(self._get_input_value(input_addr_id))
            if register_addr == -1:
                return None

            register_offset = int(self._get_input_value(self.PIN_I_REG_OFFSET))
            register_addr += register_offset

            if not 0 <= register_addr <= 65535:  # Skip: Neg. values skips register execution
                self.LOGGER.warning("Modbus register out of bounds: " + str(register_addr))
                return None

            register_read_type = self._get_input_value(input_reg_read_type)
            register_settings = self.data_types.get(self._get_input_value(input_reg_datatype))
            if register_settings is None:  # No matching type entry found. lets skip over
                self.log_debug("No matching data type found: ", self._get_input_value(input_reg_datatype))
                return None

            reg_fetch_size = int(register_settings.get('size'))
            if reg_fetch_size == -1:  # Strings have individual length
                reg_fetch_size = self._get_input_value(multiplier_fetchsize_input)

            if register_read_type == 1:
                result = self.client.read_coils(register_addr, unit=unit_id)
            elif register_read_type == 2:
                result = self.client.read_discrete_inputs(register_addr, unit=unit_id)
            elif register_read_type == 3:
                result = self.client.read_holding_registers(register_addr, reg_fetch_size, unit=unit_id)
            elif register_read_type == 4:
                result = self.client.read_input_registers(register_addr, reg_fetch_size, unit=unit_id)
            else:
                self.LOGGER.error("Unknown Read type " + register_read_type + " for register " + register_addr)
                return None

            if result.isError():
                self.LOGGER.error("Unable to read Modbus register " + str(register_addr) + ": " + str(result))
                self.log_debug("Output value " + str(input_num) + " with address " + str(register_addr)
                               + " of type " + self._get_input_value(input_reg_datatype), str(result))
                return None

            if register_read_type == 1 or register_read_type == 2:
                # fetch coils / discrete registers (true/false)
                raw_value = result.bits
                value = result.bits[0]
                self._set_output_value(pin_output_num_id, int(value))
            else:
                # multi byte registers
                decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=self.byte_order(),
                                                         wordorder=self.word_order())
                if register_settings.get('numeric'):
                    # Fetch values. Num-Values written in num and str output, Strings only as in str output.
                    raw_value = getattr(decoder, register_settings.get('method'))()
                    value = raw_value * self._get_input_value(multiplier_fetchsize_input)
                    self._set_output_value(pin_output_num_id, value)
                else:
                    # Strings fetched with individual length
                    raw_value = getattr(decoder, register_settings.get('method'))(reg_fetch_size)
                    value = raw_value.replace('\x00', '')  # Remove null bytes

            self.log_debug("Raw value " + str(input_num) + " of type " + self._get_input_value(input_reg_datatype),
                           str(raw_value))
            self._set_output_value(pin_output_str_id, str(value))  # We set string for num and str registers.
        except Exception as e:
            if bool(self._get_input_value(self.PIN_I_ENABLE_DEBUG)):
                self.log_debug("Error values:", str(input_num) + '/' + str(self.PIN_I_REG8_REGTYP) + '/' +
                               str(self.PIN_I_REG8_DATATYPE) + '/' + str(multiplier_fetchsize_input))

                raise
            # Do nothing / just catching if not in Debug mode
        finally:
            if self.is_option_set('ReconnectAfterEachRead'):
                self.client.close()

        if self.is_option_set('Sleep100ms'):  # Sleep 100ms to let slow pairs calm down
            time.sleep(0.1)
        if self.is_option_set('Sleep500ms'):  # Sleep 100ms to let slow pairs calm down
            time.sleep(0.5)

    def word_order(self):
        if int(self._get_input_value(self.PIN_I_MODBUS_WORDORDER)) == 1:
            return Endian.Big
        else:
            return Endian.Little

    def byte_order(self):
        if int(self._get_input_value(self.PIN_I_MODBUS_BYTEORDER)) == 1:
            return Endian.Big
        else:
            return Endian.Little

    def on_init(self):
        self.interval = self.FRAMEWORK.create_interval()
        if bool(self._get_input_value(self.PIN_I_SWITCH)):
            self.interval.set_interval(self._get_input_value(self.PIN_I_FETCH_INTERVAL) * 1000, self.on_interval)
            self.interval.start()

    def on_input_value(self, index, value):
        if index == self.PIN_I_SWITCH:
            self.interval.stop()
            if bool(value):
                self.interval.set_interval(self._get_input_value(self.PIN_I_FETCH_INTERVAL) * 1000, self.on_interval)
                self.interval.start()
        elif index == self.PIN_I_FETCH_INTERVAL:
            self.interval.stop()
            self.interval.set_interval(self._get_input_value(self.PIN_I_FETCH_INTERVAL) * 1000, self.on_interval)
            if bool(self._get_input_value(self.PIN_I_SWITCH)):
                self.interval.start()
        elif index == self.PIN_I_MAN_TRIGGER and bool(value):
                self.on_interval()
        elif index == self.PIN_I_MODBUS_SLAVE_IP or index == self.PIN_I_PORT or index == self.PIN_I_SLAVE_ID:
            # Reset client. Is then regenerated with new values on next run.
            if self.client:
                self.client.close()
            self.client = None

    def is_option_set(self, option):
        current_options = self._get_input_value(self.PIN_I_OPTIONS)
        if option.lower() in current_options.lower():
            return True
        return False

    def log_debug(self, key, value):
        if bool(self._get_input_value(self.PIN_I_ENABLE_DEBUG)):
            if not self.DEBUG:
                self.DEBUG = self.FRAMEWORK.create_debug_section()

            self.DEBUG.set_value(str(key), str(value))
