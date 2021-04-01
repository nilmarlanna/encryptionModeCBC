# encryptionModeCBC
# Descrição do projeto
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

# Project description
: closed_lock_with_key: Authenticated encryption using the AES block cipher in CBC mode.

- The authenticated encryption mode (Encrypt-then-MAC, Encrypt-and-MAC or MAC-then-Encrypt).
- Secret keys are generated using the PBKDF2 function of the Crypto.Protocol.KDF module.
- The MAC (Message Authentication Code) is generated using the HMAC algorithm of the Crypto.Hash module.
- The hash function used is SHA256.
 1. Returns an AES key, based on the user-defined password, and stores the used salt value for later key recovery.
 2. Retrieves a previously generated key with the stored salt value and the password specified by the user.
 3. Generate a tag from the data, using the specified key.
 4. Encrypts the data, using the key and the authenticated encryption mode that have been specified.
 5. Decrypt the data, using the key and the authenticated encryption mode that were specified, and perform the tag verification, returning True or False, depending on the tag's validity.



