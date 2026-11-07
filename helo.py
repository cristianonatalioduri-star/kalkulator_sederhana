import tkinter as tk
from tkinter import messagebox, simpledialog
import cv2

class KasirBarcode:
    def __init__(self, root):
        self.root = root
        root.title("Aplikasi Pembayaran Barcode")
        root.geometry("720x500")
        self.produk = {
            "899100210001": ("Air mineral", 5000),
            "8991002110002": ("Roti", 8000),
        }
        self.keranjang = []
        self.total = 0
        self.detector = cv2.QRCodeDetector()

        top = tk.Frame(root)
        top.pack(fill="x", padx=10, pady=10)
        tk.Button(top, text="Scan Barcode (Kamera)", command=self.scan_barcode, bg="#4CAF50", fg="white").pack(side="right")
        tk.Button(top, text="Input Manual", command=self.input_manual).pack(side="right", padx=5)

        self.listbox = tk.Listbox(root)
        self.listbox.pack(fill="both", expand=True, padx=10)

        self.label_total = tk.Label(root, text="Total: Rp 0", font=("Arial", 14, "bold"))
        self.label_total.pack(pady=10)

    def tambah_produk(self, kode):
        if kode in self.produk:
            nama, harga = self.produk[kode]
            self.keranjang.append((nama, harga))
            self.listbox.insert("end", f"{nama} - Rp {harga}")
            self.total += harga
            self.label_total.config(text=f"Total: Rp {self.total}")
        else:
            messagebox.showwarning("Gak ada", f"Barcode {kode} gak ada")

    def scan_barcode(self):
        cap = cv2.VideoCapture(0)
        last_code = None
        while True:
            ret, frame = cap.read()
            if not ret: break
            data, bbox, _ = self.detector.detectAndDecode(frame)
            if data:
                last_code = data
                cv2.putText(frame, data, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            cv2.imshow("Scan - Tekan Q untuk keluar", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        
        cap.release()
        cv2.destroyAllWindows()
        if last_code:
            self.tambah_produk(last_code.strip())

    def input_manual(self):
        kode = simpledialog.askstring("Input", "Kode barcode:")
        if kode: self.tambah_produk(kode.strip())

if __name__ == "__main__":
    root = tk.Tk()
    KasirBarcode(root)
    root.mainloop()