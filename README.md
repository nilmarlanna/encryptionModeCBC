# encryptionModeCBC
:closed_lock_with_key: Encriptação autenticada utilizando a cifra de bloco AES no modo CBC.

- O modo de encriptação autenticada (Encrypt-then-MAC, Encrypt-and-MAC ou MAC-then-Encrypt).
- As chaves secretas são geradas utilizando a função PBKDF2 do módulo Crypto.Protocol.KDF.
- O MAC (Message Authentication Code) e gerado utilizando o algoritmo HMAC do módulo Crypto.Hash.
- A função hash utilizada e a SHA256.
 1. Retorna uma chave do AES, a partir da senha definida pelo usuário, e guarda o valor utilizado de sal para recuperaçao posterior da chave.
 2. Recupera uma chave previamente gerada com o valor armazenado do sal e a senha especificada pelo usuário.
 3. Gera uma tag a partir dos dados, utilizando a chave especificada.
 4. Encripta os dados, utilizando a chave e o modo de encriptação autenticada que foram especificados.
 5. Decripta os dados, utilizando a chave e o modo de encriptação autenticada que foram especificados, e realiza a verificação da tag, retornando True ou False, dependendo da validade da tag.


