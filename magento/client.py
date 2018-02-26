import requests
from magento import exceptions


class Client(object):
    def __init__(self, server_url, access_token):
        self.server_url = server_url
        self.access_token = access_token
        self.base_url = server_url + 'rest/V1/'

    def search_product(self, params=None):
        """Get product list

        Args:
            params:

        Returns:

        """
        return self._get('products', params=params)

    def get_product(self, product_id, params=None):
        """Get info about product by product SKU

        Args:
            product_id:
            params:

        Returns:

        """
        return self._get('products/' + product_id, params=params)

    def create_product(self, data=None):
        """Create product

        Args:
            data:

        Returns:

        """
        return self._post('products', json=data)

    def update_product(self, product_id, data=None):
        """Create product

        Args:
            product_id:
            data:

        Returns:

        """
        return self._put('products/' + product_id, json=data)

    def delete_product(self, product_id, params=None):
        """Delete product by product SKU

        Args:
            product_id:
            params:

        Returns:

        """
        return self._delete('products/' + product_id, params=params)

    def search_customer(self, params=None):
        """Retrieve customers which match a specified criteria. This call returns an array of objects,
        but detailed information about each object’s attributes might not be included.
        See http://devdocs.magento.com/codelinks/attributes.html#CustomerRepositoryInterface to
        determine which call to use to get detailed information about all attributes for an object.

        Args:
            params:

        Returns:

        """
        return self._get('customers/search', params=params)

    def get_customer(self, customer_id, params=None):
        """Get customer by Customer ID.

        Args:
            customer_id:
            params:

        Returns:

        """
        return self._get('customers/' + customer_id, params=params)

    def create_customer(self, data=None):
        """Create customer

        Args:
            data:

        Returns:

        """
        return self._post('customers', json=data)

    def update_customer(self, customer_id, data=None):
        """Create or update a customer.

        Args:
            customer_id:
            data:

        Returns:

        """
        return self._put('customers/' + customer_id, json=data)

    def delete_customer(self, product_id, params=None):
        """Delete customer by Customer ID.

        Args:
            product_id:
            params:

        Returns:

        """
        return self._delete('customers/' + product_id, params=params)

    def search_order(self, params=None):
        """Lists orders that match specified search criteria. This call returns an array of objects,
        but detailed information about each object’s attributes might not be included.
        See http://devdocs.magento.com/codelinks/attributes.html#OrderRepositoryInterface to determine
        which call to use to get detailed information about all attributes for an object.

        Args:
            params:

        Returns:

        """
        return self._get('orders', params=params)

    def get_order(self, order_id, params=None):
        """Loads a specified order.

        Args:
            order_id:
            params:

        Returns:

        """
        return self._get('orders/' + order_id, params=params)

    def _get(self, url, **kwargs):
        return self._request('GET', url, **kwargs)

    def _post(self, url, **kwargs):
        return self._request('POST', url, **kwargs)

    def _put(self, url, **kwargs):
        return self._request('PUT', url, **kwargs)

    def _patch(self, url, **kwargs):
        return self._request('PATCH', url, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request('DELETE', url, **kwargs)

    def _request(self, method, endpoint, headers=None, **kwargs):
        _headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        if headers:
            _headers.update(headers)
        return self._parse(requests.request(method, self.base_url + endpoint, headers=_headers, **kwargs))

    def _parse(self, response):
        status_code = response.status_code
        if 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            r = response.text
        if status_code in (200, 201, 202):
            return r
        elif status_code == 204:
            return None
        elif status_code == 400:
            raise exceptions.BadRequestError(r)
        elif status_code == 401:
            raise exceptions.UnauthorizedError(r)
        elif status_code == 403:
            raise exceptions.ForbiddenError(r)
        elif status_code == 404:
            raise exceptions.NotFoundError(r)
        elif status_code == 405:
            raise exceptions.NotAllowedError(r)
        elif status_code == 406:
            raise exceptions.NotAcceptableError(r)
        elif status_code == 500:
            raise exceptions.SystemError(r)
        else:
            raise exceptions.UnknownError(r)
