
#!/usr/bin/env python3

import os
import sys

def check_root():
    if os.getuid() != 0:
        print("\033[91mError: يجب تشغيل السكريبت كـ root!\033[0m")
        print("\033[93mطريقة الاستخدام:\033[0m")
        print("  sudo ./test.py")
        print("  أو:")
        print("  sudo python3 test.py")
        sys.exit(1)

if __name__ == "__main__":
    check_root()
    print("\033[92mتم التشغيل كـ root بنجاح!\033[0m")
    # أكوادك هنا
