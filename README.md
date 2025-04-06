
# Projekat Online Sales Analysis

Ovaj projekat je dizajniran za upravljanje osnovnim inventarom proizvoda, upravljanje korpom kupca i izračunavanje ukupne vrednosti inventara i korpe. Projekat se sastoji od nekoliko Python klasa koje omogućavaju korisnicima da upravljaju proizvodima i njihovim količinama, kao i da komuniciraju sa korpom kupca.

## Klase

### 1. `Product`
- **Atributi:**
  - `name`: Ime proizvoda.
  - `price`: Cena proizvoda.
  - `quantity`: Količina proizvoda.
- **Metode:**
  - `display_product_info()`: Prikazuje informacije o proizvodu (ime, cena, količina).
  - `update_quantity(new_quantity)`: Ažurira količinu proizvoda.

### 2. `ProductManager`
- **Atributi:**
  - `products`: Lista svih dostupnih proizvoda.
- **Metode:**
  - `add_product(product)`: Dodaje proizvod u inventar.
  - `display_all_products()`: Prikazuje sve proizvode u inventaru.
  - `total_inventory_value()`: Izračunava ukupnu vrednost svih proizvoda u inventaru.

### 3. `Cart`
- **Atributi:**
  - `cart_items`: Lista proizvoda u korpi.
- **Metode:**
  - `add_to_cart(product)`: Dodaje proizvod u korpu.
  - `calculate_cart_value()`: Izračunava ukupnu vrednost korpe.
  - `display_cart_contents()`: Prikazuje sadržaj korpe.

## Pregled projekta

Projekat omogućava korisnicima da:
1. Upravljaju inventarom proizvoda koristeći klase `Product` i `ProductManager`.
2. Dodaju proizvode u korpu i izračunavaju ukupnu vrednost koristeći klasu `Cart`.

Ovaj projekat može biti proširen sa funkcijama kao što su upravljanje porudžbinama, checkout i druge.
