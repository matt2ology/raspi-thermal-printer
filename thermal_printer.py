# thermal_printer.py
from escpos.printer import Usb
import textwrap

class ThermalPrinter:
    # Constants for printer configuration
    DEFAULT_VENDOR_ID: int = 0x0fe6
    DEFAULT_PRODUCT_ID: int = 0x811e
    DEFAULT_INTERFACE: int = 0
    DEFAULT_IN_EP: int = 0x81
    DEFAULT_OUT_EP: int = 0x01
    DEFAULT_TIMEOUT_MS: int = 5000

    # Constants for text formatting
    DEFAULT_PRINT_AREA_PIXELS: int = 570       # maximum printable width in pixels
    DEFAULT_FONT_PIXEL_WIDTH: int = 12         # width of one character in pixels (Font A)

    def __init__(
        self,
        idVendor: int = DEFAULT_VENDOR_ID,
        idProduct: int = DEFAULT_PRODUCT_ID,
        interface: int = DEFAULT_INTERFACE,
        in_ep: int = DEFAULT_IN_EP,
        out_ep: int = DEFAULT_OUT_EP,
        timeout: int = DEFAULT_TIMEOUT_MS,
        font_pixel_width: int = DEFAULT_FONT_PIXEL_WIDTH,
        print_area_pixels: int = DEFAULT_PRINT_AREA_PIXELS
    ) -> None:
        """
        Initialize the USB thermal printer.
        """
        self._printer: Usb = Usb(
            idVendor=idVendor,
            idProduct=idProduct,
            interface=interface,
            in_ep=in_ep,
            out_ep=out_ep,
            timeout=timeout
        )
        self._font_pixel_width: int = font_pixel_width
        self._print_area_pixels: int = print_area_pixels


    def __getattr__(self, name: str):
        """
        Delegate method calls to the underlying Usb printer instance.
        """
        return getattr(self._printer, name)

    def _wrap_text(self, text: str) -> str:
        """
        Private method: Wrap the input text so that it fits within the printer's maximum print area.

        Each line is wrapped according to the printer's font width and print area,
        ensuring that the text does not exceed the printable width.

        Parameters:
            text (str): The text to be wrapped for printing.

        Returns:
            str: The text with line breaks inserted at appropriate positions.

        Output (example):
            This is a long line that will be
            wrapped to fit the printer width.
        """
        max_chars_per_line = self._print_area_pixels // self._font_pixel_width
        wrapped_text: str = textwrap.fill(text, width=max_chars_per_line)
        return wrapped_text

    def print_text(self, text: str):
        """
        Public method: Print text on the thermal printer after wrapping lines to fit the print area.

        Example:
            printer = ThermalPrinter()
            printer.print_text("This is a long line that will automatically wrap to fit the printer width.")
        """
        wrapped_text = self._wrap_text(text)
        self._printer.text(wrapped_text)

# Example usage
if __name__ == "__main__":
    printer: ThermalPrinter = ThermalPrinter() # printer = ThermalPrinter()
    long_text: str = (
        "This is a very long text that should wrap properly at the printer's maximum width "
        "based on the font size and print area."
    )
    printer.text("Hello World")  # directly call Usb methods
    printer.ln(5)
    printer.print_text(long_text)
    printer.cut()
