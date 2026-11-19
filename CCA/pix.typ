// "Pix copia e cola" estático (BR Code, padrão EMV do Banco Central),
// sem valor fixo: quem escaneia digita quanto quer contribuir.

// CRC16-CCITT-FALSE (polinômio 0x1021, início 0xFFFF), exigido no campo 63.
// Valor de referência: crc16("123456789") == "29B1".
#let crc16(s) = {
  let crc = 0xFFFF
  for b in array(bytes(s)) {
    crc = crc.bit-xor(b.bit-lshift(8))
    for _ in range(8) {
      crc = if crc.bit-and(0x8000) != 0 {
        crc.bit-lshift(1).bit-xor(0x1021).bit-and(0xFFFF)
      } else {
        crc.bit-lshift(1).bit-and(0xFFFF)
      }
    }
  }
  let h = upper(str(crc, base: 16))
  "0" * (4 - h.len()) + h
}

// Campo EMV: id de 2 dígitos + tamanho de 2 dígitos + valor.
#let campo(id, valor) = {
  assert(valor.len() < 100, message: "campo " + id + " longo demais")
  let n = str(valor.len())
  id + "0" * (2 - n.len()) + n + valor
}

// chave: CPF só com dígitos, e-mail, telefone +55… ou chave aleatória.
// nome (≤ 25) e cidade (≤ 15) em ASCII maiúsculo, sem acento.
#let pix-payload(chave, nome, cidade) = {
  assert(nome.len() <= 25, message: "nome do recebedor passa de 25 caracteres")
  assert(cidade.len() <= 15, message: "cidade passa de 15 caracteres")
  let p = (
    campo("00", "01")
    + campo("26", campo("00", "br.gov.bcb.pix") + campo("01", chave))
    + campo("52", "0000")
    + campo("53", "986")
    + campo("58", "BR")
    + campo("59", nome)
    + campo("60", cidade)
    + campo("62", campo("05", "***"))
    + "6304"
  )
  assert(p.len() == p.clusters().len(), message: "BR Code precisa ser ASCII (tire os acentos)")
  p + crc16(p)
}
