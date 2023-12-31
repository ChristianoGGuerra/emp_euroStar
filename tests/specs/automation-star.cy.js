/// <reference types="cypress" />
import { url } from '../helpers/common.helper';
import addrPages from '../page/address';
import listOfAddressAddedPage from '../page/addr-result';

Cypress.on('uncaught:exception', (err, runnable) => { return false });

describe('AutomationStar -> Address Functional Test', () => {
    beforeEach(() => cy.visit(`${url}`));

    it('Should have Address Creation Page as a title', () => {
        cy.get('.panel-title').should('have.text', 'Address Creation Page');
    });

    it('Should check all information text, inputs and button', () => {
        addrPages.streetAddrLabel().should('contain.text', 'Street name:');
        addrPages.streetAddrInput().should('have.attr', 'placeholder', 'Add the street name...');

        addrPages.streetNumberLabel().should('contain.text', 'Number:');
        addrPages.streetNumberInput().should('have.attr', 'placeholder', 'Add the number...');

        addrPages.streetOtherInfoLabel().should('contain.text', 'More Address Information:');
        addrPages.streetOtherInfoInput().should('have.attr', 'placeholder', 'Other Address Information...');

        addrPages.cityLabel().should('contain.text', 'City:');
        addrPages.cityInput().should('have.attr', 'placeholder', 'Add the name of the city...');

        addrPages.countyLabel().should('contain.text', 'County or State:');
        // addrPages.countyInput().should('have.attr', 'placeholder', 'Add the name of the county/state...');

        addrPages.countryLabel().should('contain.text', 'Country:');
        addrPages.countrySelector().select(0).children().eq(0).should('have.text', '---------');

        addrPages.zipCodeLabel().should('contain.text', 'Zip Code:');
        addrPages.zipCodeInput().should('have.attr', 'placeholder', 'Add the zip code...');
    });

    describe('AutomationStar Accessibility', () => {
        beforeEach(() => {
            cy.injectAxe();
        });
    
        it('Should have no detectable a11y errors on page', () => {
            cy.checkA11y();
        });

        it('Should check accessibility using desktop sizes - MacBook 16 and MacBook 11', () => {
            cy.devicesResizing('macbook-11', 'macbook-16');
            cy.checkA11y();
        });

        it('Should check accessibility using Iphone X and Samsung S10', () => {
            cy.devicesResizing('iphone-x', 'samsung-s10');
            cy.checkA11y();
        });

        it('Should check accessibility using Ipad 2 and Samsung Note 9', () => {
            cy.devicesResizing('ipad-2', 'samsung-note9');
            cy.checkA11y();
        });

        it('Should be able to use only keyboard', () => {
            cy.get('body').tab().then(() => {
                addrPages.streetAddrInput().should('be.focused');
                addrPages.streetAddrInput().type('Sonnenallee street');
            });
            addrPages.streetAddrInput().tab().then(() => {
                addrPages.streetNumberInput().should('be.focused');
                addrPages.streetNumberInput().type('10');
            });
            addrPages.streetNumberInput().tab().then(() => {
                addrPages.streetOtherInfoInput().should('be.focused');
                addrPages.streetOtherInfoInput().type('Automation Star Conference Nº floor')
            });
            addrPages.streetOtherInfoInput().tab().then(() => {
                addrPages.cityInput().should('be.focused');
                addrPages.cityInput().type('Berlin');
            });
            addrPages.cityInput().tab().then(() => {
                addrPages.countyInput().should('be.focused');
                addrPages.countyInput().type('Brandenburg');
            });
            addrPages.countyInput().tab().then(() => {
                addrPages.countrySelector().should('be.focused')
                addrPages.countrySelector().select(82);

            });
            addrPages.countrySelector().tab().then(() => {
                addrPages.zipCodeInput().should('be.focused');
                addrPages.zipCodeInput().type('4050-123');
            });
            addrPages.zipCodeInput().tab().then(() => {
                addrPages.submitButton().should('be.focused');
                addrPages.submitButton().click();
            });
            cy.url().should('include', '/address/result/');
            listOfAddressAddedPage.title().should('contain.text', 'had been added with success!');
            listOfAddressAddedPage
            .listOfAddrs()
            .eq(0)
            .should('have.text', 'Sonnenallee street - 10, Automation Star Conference Nº floor; City: Berlin - County: Brandenburg - Country: Germany');
        });
    });
});
  
