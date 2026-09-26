# Local currency and the parallel currencies of a company code

**Level:** 201 · for FI consultants

**One line:** Every company code has exactly one local currency, and up to two more that are carried on every line item in BSEG — in ECC via OB22, in S/4HANA via FINSC_LEDGER — which is why the choice is nearly impossible to change after go-live.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- Local currency: T001-WAERS, OBY6, and the amount fields BSEG-DMBTR / ACDOCA-HSL
- Second and third local currency: OB22 and T001A in ECC, the 1st/2nd/3rd FI currency columns of FINSC_LEDGER in S/4HANA, BSEG-DMBE2 / DMBE3
- Source currency for translation: translate from document currency or from the first local currency, and why it matters for exchange rate differences
- Exchange rate type and translation date type per parallel currency
- What is BSEG-relevant and what lives only in ACDOCA

## Related pages

- [Currency types: 00, 10, 30, 40, 50, 60 and the Z types](../currency_types/README.md)
- [Currencies in the Universal Journal (ACDOCA)](../universal_journal_currencies/README.md)
- [Ledgers and their currencies: FINSC_LEDGER](../ledgers_and_currencies/README.md)
- [Exchange rates: TCURR, rate types, quotation and translation dates](../exchange_rates/README.md)
- [Introducing, changing and retiring currencies](../introducing_and_changing_currencies/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
