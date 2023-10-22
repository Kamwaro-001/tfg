import axios from 'axios';

export const get_trees = async () => {
	/** @type {AxiosResponse<any>} */
	const response = await axios.get('/api/plant/');
	return response.data;
};

export const add_tree = async (/** @type {any} */ tree) => {
	try {
		await axios.post('/api/plant/', tree);

		return {
			message: 'success'
		};
	} catch (/** @type {any} */ error) {
		return {
			message: error.message
		};
	}
};

export const delete_tree = async (/** @type {any} */ tree_id) => {
	try {
		await axios.delete('/api/plant/', tree_id);

		return {
			message: 'tree deleted'
		};
	} catch (/** @type {any} */ error) {
		return {
			message: error.message
		};
	}
}