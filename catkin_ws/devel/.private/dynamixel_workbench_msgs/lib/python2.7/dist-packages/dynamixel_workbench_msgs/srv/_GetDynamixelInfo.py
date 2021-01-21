# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dynamixel_workbench_msgs/GetDynamixelInfoRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetDynamixelInfoRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "dynamixel_workbench_msgs/GetDynamixelInfoRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# It is Served by 'single_dynamixel_monitor' node
# This message is used to get information of dynamixel

"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetDynamixelInfoRequest, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dynamixel_workbench_msgs/GetDynamixelInfoResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import dynamixel_workbench_msgs.msg

class GetDynamixelInfoResponse(genpy.Message):
  _md5sum = "5075be00278efc6e6ba91f48b43afb53"
  _type = "dynamixel_workbench_msgs/GetDynamixelInfoResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
DynamixelInfo dynamixel_info


================================================================================
MSG: dynamixel_workbench_msgs/DynamixelInfo
# This message includes information of dynamixel's basic parameter

DynamixelLoadInfo load_info

string model_name
uint16 model_number
uint8 model_id


================================================================================
MSG: dynamixel_workbench_msgs/DynamixelLoadInfo
# This message includes dynamixel's load information

string device_name
uint64 baud_rate
float32 protocol_version
"""
  __slots__ = ['dynamixel_info']
  _slot_types = ['dynamixel_workbench_msgs/DynamixelInfo']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       dynamixel_info

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetDynamixelInfoResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.dynamixel_info is None:
        self.dynamixel_info = dynamixel_workbench_msgs.msg.DynamixelInfo()
    else:
      self.dynamixel_info = dynamixel_workbench_msgs.msg.DynamixelInfo()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.dynamixel_info.load_info.device_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_Qf().pack(_x.dynamixel_info.load_info.baud_rate, _x.dynamixel_info.load_info.protocol_version))
      _x = self.dynamixel_info.model_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_HB().pack(_x.dynamixel_info.model_number, _x.dynamixel_info.model_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.dynamixel_info is None:
        self.dynamixel_info = dynamixel_workbench_msgs.msg.DynamixelInfo()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.dynamixel_info.load_info.device_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.dynamixel_info.load_info.device_name = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.dynamixel_info.load_info.baud_rate, _x.dynamixel_info.load_info.protocol_version,) = _get_struct_Qf().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.dynamixel_info.model_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.dynamixel_info.model_name = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.dynamixel_info.model_number, _x.dynamixel_info.model_id,) = _get_struct_HB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.dynamixel_info.load_info.device_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_Qf().pack(_x.dynamixel_info.load_info.baud_rate, _x.dynamixel_info.load_info.protocol_version))
      _x = self.dynamixel_info.model_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_HB().pack(_x.dynamixel_info.model_number, _x.dynamixel_info.model_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.dynamixel_info is None:
        self.dynamixel_info = dynamixel_workbench_msgs.msg.DynamixelInfo()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.dynamixel_info.load_info.device_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.dynamixel_info.load_info.device_name = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.dynamixel_info.load_info.baud_rate, _x.dynamixel_info.load_info.protocol_version,) = _get_struct_Qf().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.dynamixel_info.model_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.dynamixel_info.model_name = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.dynamixel_info.model_number, _x.dynamixel_info.model_id,) = _get_struct_HB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_HB = None
def _get_struct_HB():
    global _struct_HB
    if _struct_HB is None:
        _struct_HB = struct.Struct("<HB")
    return _struct_HB
_struct_Qf = None
def _get_struct_Qf():
    global _struct_Qf
    if _struct_Qf is None:
        _struct_Qf = struct.Struct("<Qf")
    return _struct_Qf
class GetDynamixelInfo(object):
  _type          = 'dynamixel_workbench_msgs/GetDynamixelInfo'
  _md5sum = '5075be00278efc6e6ba91f48b43afb53'
  _request_class  = GetDynamixelInfoRequest
  _response_class = GetDynamixelInfoResponse
