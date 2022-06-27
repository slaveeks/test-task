import {SortedData} from './types/SortedData';
import {TotalSum} from './types/TotalSum';

/**
 * Transport class
 *
 */
export class Transport {
  /**
   * Get sum of orders
   *
   * @return {Promise<TotalSum>} - response
   */
  public static async getSumOfOrders():
      Promise<TotalSum> {
    const response = await fetch('http://127.0.0.1:5000/todo/api/v1.0/sum', {
      method: 'GET',
      headers: {
        accept: 'application/json',
      },
    });
    return await response.json();
  }

  /**
   * Get all data
   *
   * @return {Promise<any>} - response
   */
  public static async getAllData(): Promise<any> {
    const response = await fetch('http://127.0.0.1:5000/todo/api/v1.0/all_data', {
      method: 'GET',
      headers: {
        accept: 'application/json',
      },
    });
    return await response.json();
  }

  /**
   * Get ordered data
   *
   * @return {Promise<any>} - response
   */
  public static async getOrderedData(): Promise<SortedData | undefined> {
    const response = await fetch('http://127.0.0.1:5000/todo/api/v1.0/ordered_data', {
      method: 'GET',
      headers: {
        accept: 'application/json',
      },
    });
    return await response.json();
  }
}

