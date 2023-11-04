/*
AutomationStart Berlins 20-21 NOV. 2023
Automation for Accessibility – A Real Challenge
Thiago Machado & Christiano Guerra
*/

// For any command it is necessary only add a command as described below.
/*
import address from '../page/address';

Cypress.Commands.add('create-addr', (streetName, number, otherInfo, city, county, country, zCode) => {
   address.nameOfStreet().type(streetName);
   address.streetNumber().type(number);
   address.otherAddressInformations().type(otherInfo);
   address.city().type(city);
   address.county().type(county);
   address.country().select(country);
   address.zCode().type(zCode);
});
*/
Cypress.Commands.add('devicesResizing', (type1, type2) => {
   const sizes = [type1, type2];

   sizes.forEach((size) => {
         cy.viewport(size);
         cy.checkA11y();
   });
});
