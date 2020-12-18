# bip39tgen: 12-word BIP39 mnemonic generator

bip39tgen is a small command-line tool written in Python to generate random 12-word English mnemonics in the BIP39 format. Its output can be imported to cryptocurrency (e.g. Bitcoin, Ethereum) wallets (e.g. Jaxx Liberty, Electrum, MyCrypto) to generate an infinite sequence of addresses and secret keys.

See the [BIP39 specification](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#Generating_the_mnemonic) for the format of the 12-word mnemonic.

Run bip39tgen on a trusted machine when nobody's whatching, and note the generated 12-word mnemonic securely (e.g. on a piece of paper, and store it securely). It can be used to spend (transfer) all your cryptocurrency, and you don't want hackers to do that. Don't type it to any web page, and don't type it on any computer or mobile device which you don't trust.

The generated 12-word mnemonic contains 128 bits of entropy and 4 bits of checksum.
