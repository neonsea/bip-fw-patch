# fw_patch

Amazfit Bip Firmware Patch Tool with patches

## Contents

Python script for patching:

* fw_patcher.py

Patch to redirect Alipay debug messages to the standard log service:

* alipay_debug.patch (latin 1.1.5.36)

Patch for data exchange via BLE Service:

* alipay_subst.patch (latin 1.1.5.36)
* bipos_subst.patch (non-latin 1.1.2.05)

These patches let you use the [alipay-bt library](https://github.com/neonsea/alipay-bt). An example application can be found [here](https://github.com/neonsea/bt-template).

## Thanks

* x27 ([research](https://github.com/freebip/bt_echo))
* MNVolkov (libbip)