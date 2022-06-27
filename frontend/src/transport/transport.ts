import {SortedData} from './types/SortedData';

/**
 * Transport class
 *
 */
export class Transport {
  /**
   * Get sum of orders
   *
   * @return {Promise<any>} - response
   */
  public static async getSumOfOrders():
      Promise<Array<Array<number | string>> | null> {
    const response = await fetch('http://127.0.0.1:5000/todo/api/v1.0/sum');
    console.log(response);
    return await response.json();
  }

  /**
   * Get all data
   *
   * @return {Promise<any>} - response
   */
  public static async getAllData(): Promise<any> {
    const response = await fetch('http://127.0.0.1:5000/todo/api/v1.0/all_data');
    return await response.json();
  }

  /**
   * Get ordered data
   *
   * @return {Promise<any>} - response
   */
  public static async getOrderedData(): Promise<SortedData | undefined> {
    const response = await fetch('http://127.0.0.1:5000/todo/api/v1.0/ordered_data');
    return await response.json();
  }
}

