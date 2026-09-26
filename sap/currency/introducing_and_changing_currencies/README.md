# Introducing, changing and retiring currencies

**Level:** 301 · for architects and anyone who has been asked to "just add a currency"

**One line:** Adding a currency *key* is a table entry; adding a currency *type* to a live company code is a data conversion project, because every historical line would have to be re-valued — the one setting SAP itself says cannot be introduced by migration.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- Adding a new currency key: TCURC, TCURX, TCURT, rates, and the codes that changed recently (VES/VED, SLE, ZWL/ZWG, STN, MRU)
- Changing the local currency of a company code: why it is a project, not a setting
- Adding a freely defined currency type since S/4HANA 1809: the Manage Currencies tools in the IMG, and the BSEG-relevance limit
- Currency changeover (EMU / euro) and redenomination: the conversion tools and what they do to open items
- Migration to S/4HANA: what the currency configuration migration does and does not do (note 2344012)
- Retiring a currency and closing accounts in it

## Related pages

- [Currency keys, codes and decimal places](../currency_keys_and_decimals/README.md)
- [Local currency and the parallel currencies of a company code](../local_and_parallel_currencies/README.md)
- [Currencies in the Universal Journal (ACDOCA)](../universal_journal_currencies/README.md)
- [Ledgers and their currencies: FINSC_LEDGER](../ledgers_and_currencies/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
