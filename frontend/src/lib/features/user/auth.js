import axios from 'axios';

export const header = 'http://127.0.0.1:8000';

export const set_auth_header = (/** @type {string} */ token) => {
	if (typeof token !== 'undefined' && token) {
		axios.defaults.headers.common['Authorization'] = 'Token ' + token;
	} else {
		delete axios.defaults.headers.common['Authorization'];
	}
}

export const login = async (/** @type {object} */ form_data) => {
	/** @type {AxiosResponse<any>} */
	const response = await axios.post('/api/accounts/jwt/create/', form_data);
	return response.data;
};

export const signup = async (/** @type {any} */ formdata) => {
	try {
		const { username, first_name, last_name, phone_number, town, county, email, password, re_password } = formdata;
		return (
			await axios.post(`${header + '/api/accounts/users/'}`, {
				username,
				first_name,
				last_name,
				phone_number,
				town,
				county,
				email,
				password,
				re_password
			}),
			{
				message: 'success'
			}
		);
	} catch (/** @type {any} */ error) {
		return {
			message: error.message
		};
	}
};


