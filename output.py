#!/usr/bin/env python
# timestamp: 2025-03-10 07:56:36
# author: alterkleo
# engine: hexcore v2.5.0

import marshal as m,zlib as z
_=bytes([120, 218, 123, 204, 128, 4, 152, 161, 244, 103, 45, 32, 49, 149, 33, 152, 65, 138, 161, 136, 33, 134, 81, 137, 33, 152, 209, 148, 17, 34, 85, 196, 20, 195, 160, 196, 16, 195, 4, 227, 43, 48, 164, 51, 105, 50, 39, 51, 34, 153, 194, 2, 53, 233, 179, 12, 216, 148, 104, 184, 92, 48, 99, 40, 131, 41, 19, 92, 31, 131, 38, 147, 95, 21, 155, 71, 106, 78, 78, 190, 142, 38, 227, 45, 214, 130, 162, 204, 188, 18, 32, 131, 37, 47, 49, 55, 181, 24, 164, 75, 225, 22, 167, 77, 70, 106, 69, 114, 126, 81, 170, 221, 45, 150, 220, 196, 204, 188, 34, 54, 160, 48, 200, 136, 98, 30, 32, 209, 192, 112, 135, 133, 179, 67, 99, 130, 203, 85, 22, 201, 207, 32, 83, 171, 132, 194, 51, 18, 75, 20, 50, 139, 21, 42, 243, 75, 139, 20, 64, 6, 217, 251, 105, 50, 131, 117, 221, 98, 205, 204, 43, 40, 45, 41, 2, 57, 111, 37, 67, 17, 59, 200, 51, 172, 32, 113, 14, 155, 220, 252, 148, 210, 156, 84, 187, 34, 46, 32, 23, 100, 111, 177, 28, 144, 248, 192, 204, 200, 200, 248, 137, 133, 145, 81, 234, 35, 27, 3, 7, 239, 5, 94, 197, 203, 236, 74, 13, 44, 15, 25, 88, 26, 66, 90, 185, 192, 250, 1, 107, 47, 59, 17])
def __():
 try:
  return m.loads(z.decompress(_))
 except:
  print("error: failed to decode")
  return None
exec(__(),globals())