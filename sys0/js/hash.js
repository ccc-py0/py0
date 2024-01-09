import { encodeHex } from "https://deno.land/std@0.207.0/encoding/hex.ts";

export async function hash(text, method='SHA-256') {
  let buf = new TextEncoder().encode(text)
  let buf2 = await crypto.subtle.digest(method, buf)
  return encodeHex(buf2)
}

// console.log(await hash('hello'))
