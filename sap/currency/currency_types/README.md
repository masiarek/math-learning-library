# Currency types: 00, 10, 30, 40, 50, 60 and the Z types

**Level:** 201 · for consultants and developers who have to read ACDOCA or configure a ledger

**One line:** A currency *key* says which money; a currency *type* says which *role* an amount plays — document, company code, group, hard, index-based, global company or freely defined — and every amount field in the journal is one role, not one key.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- The standard types: 00 document, 10 company code, 30 group, 40 hard, 50 index-based, 60 global company, 70 controlling area object currency
- Where each type gets its key: client (SCC4), country (OY01), company (OX15), company code (OBY6), controlling area (OKKP)
- Freely defined currency types Y*/Z* in S/4HANA and what they can and cannot be used for
- Currency type versus currency key: why two documents in EUR can have different types, and one type can hold different keys
- The valuation view in the currency type: legal, group and profit-center valuation (10, 11, 12 …)

## Related pages

- [Local currency and the parallel currencies of a company code](../local_and_parallel_currencies/README.md)
- [Currencies in the Universal Journal (ACDOCA)](../universal_journal_currencies/README.md)
- [Ledgers and their currencies: FINSC_LEDGER](../ledgers_and_currencies/README.md)
- [Currencies in Controlling and margin analysis](../controlling_currencies/README.md)
- [Material Ledger: parallel currencies and valuations for inventory](../material_ledger_currencies/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
