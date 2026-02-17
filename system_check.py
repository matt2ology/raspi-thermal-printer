import subprocess
import logging


class SystemCheck:

    @staticmethod
    def check_libusb_package():
        result = subprocess.run(
            ["dpkg-query", "-W", "-f=${Status}", "libusb-1.0-0"],
            capture_output=True,
            text=True
        )

        installed = (
            result.returncode == 0
            and "install ok installed" in result.stdout
        )

        if installed:
            logging.info("libusb-1.0-0 package is installed")
        else:
            logging.error("libusb-1.0-0 package is NOT installed")

        return installed

    @staticmethod
    def check_pyusb_runtime():
        try:
            import usb.core
            devices = list(usb.core.find(find_all=True))
            logging.info("libusb runtime OK (%d USB devices found)", len(devices))
            return True
        except Exception as e:
            logging.exception("libusb runtime check failed: %s", e)
            return False

    @classmethod
    def system_ready(cls):
        return cls.check_libusb_package() and cls.check_pyusb_runtime()
