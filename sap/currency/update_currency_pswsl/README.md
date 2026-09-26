# Update currency: BSEG-PSWSL and BSEG-PSWBT

**Level:** 301 · for anyone who has seen FS10N and FBL3N disagree

**One line:** Besides the document currency and the local currencies, every G/L line carries a fourth pair, the *update currency* and its amount, and it is this pair — not the document currency — that the balance tables GLT0, FAGLFLEXT and ACDOCA-TSL are kept in.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- The four currency pairs on a line item: WAERS/WRBTR, HWAER/DMBTR, DMBE2/DMBE3, and PSWSL/PSWBT
- Why balances need an update currency at all: transaction figures per account and currency
- The rule: SKB1-XSALH set means local currency, otherwise document currency, except in a clearing
- The clearing exception: the balance in update currency of an open-item account must return to zero
- The ABAP behind it: SAPMF05A, FORM KDFTAB_ABARBEITEN, and the same test in exchange rate difference lines
- GLT0-TSL, FAGLFLEXT-TSL and ACDOCA-TSL versus HSL; RTCUR is not the document currency
- A program that derives PSWSL/PSWBT for every case and shows the balances that result

## Related pages

- ["Only manage balances in local currency" (SKB1-XSALH)](../only_balances_in_local_currency/README.md)
- [Exchange rate differences on clearing (realized gains and losses)](../exchange_rate_differences_on_clearing/README.md)
- [Currencies in the Universal Journal (ACDOCA)](../universal_journal_currencies/README.md)
- [Reporting and troubleshooting currency questions](../reporting_and_troubleshooting/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
