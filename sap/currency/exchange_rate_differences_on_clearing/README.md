# Exchange rate differences on clearing (realized gains and losses)

**Level:** 201 · for FI consultants and accountants

**One line:** When an open item posted at one rate is cleared at another, the local-currency amounts no longer net to zero, and the system posts the gap automatically to the accounts in OBA1 — realized, because the cash has moved.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- Realized versus unrealized differences, and which transaction posts which
- Account determination: OBA1, transaction keys KDF (open items), KDB (G/L accounts without open items), KDW, KDZ, and the reconciliation account link
- Partial payments, residual items, cash discount and the difference that goes with each
- T001-XSLTA and the case where no difference should be posted
- The update currency of the difference line: PSWSL/PSWBT in the KDF line, from SAPMF05A
- Parallel currencies: a difference in DMBE2 but not in DMBTR, and vice versa
- Reset of a clearing and why the difference document has to be reversed

## Related pages

- [Update currency: BSEG-PSWSL and BSEG-PSWBT](../update_currency_pswsl/README.md)
- ["Only manage balances in local currency" (SKB1-XSALH)](../only_balances_in_local_currency/README.md)
- [Foreign currency valuation and translation (unrealized differences)](../foreign_currency_valuation/README.md)
- [Exchange rates: TCURR, rate types, quotation and translation dates](../exchange_rates/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
