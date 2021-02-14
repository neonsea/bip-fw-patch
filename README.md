## fw_patch
Amazfit Bip Firmware Patch Tool with patches

python script for patching

* fw_patcher.py

patch to redirect Alipay debug messages to the standard log service

* alipay_debug.patch (latin 1.1.5.36)

patch for data exchange via BLE Service

* alipay_subst.patch (latin 1.1.5.36)
* bipos_subst.patch (non-latin 1.1.2.05)

these patches let you use the [alipay-bt library](https://github.com/neonsea/libbip/blob/master/alipay-bt.h)

thanks to:
* x27 (research)
* MNVolkov (libbip)