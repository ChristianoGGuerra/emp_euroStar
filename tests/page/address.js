const addrPages = {
    streetAddrInput: () => cy.get('#id_address_line1'),
    streetAddrLabel: () => cy.get('#id_address_line1').parent(),
    streetNumberInput: () => cy.get('#id_number'),
    streetNumberLabel: () => cy.get('#id_number').parent(),
    streetOtherInfoInput: () => cy.get('#id_others'),
    streetOtherInfoLabel: () => cy.get('#id_others').parent(),
    cityInput: () => cy.get('#id_city'),
    cityLabel: () => cy.get('#id_city').parent(),
    countyInput: () => cy.get('#id_county'),
    countyLabel: () => cy.get('#id_county').parent(),
    countrySelector: () => cy.get('#id_country'),
    countryItemSelector: () => cy.get('#id_country'),
    countryLabel: () => cy.get('#id_country').parent(),
    zipCodeInput: () => cy.get('#id_zip_code'),
    zipCodeLabel: () => cy.get('#id_zip_code').parent(),
    submitButton: () => cy.get('.submit')
}

export default addrPages;