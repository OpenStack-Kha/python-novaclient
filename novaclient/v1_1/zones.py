from novaclient import base

class Zone(base.Resource):
    """
    A Zone.
    """
    def __repr__(self):
        if hasattr(self, 'id'):
            return "<Zone: id=%s, name=%s>" % (self.id, self.name)
        elif hasattr(self,'node_id'):
            return "<Zone: name=%s, Node id=%s>" % (self.zone_name, self.node_id)


class ZoneManager(base.ManagerWithFind):
    """
    Manage :class:`Zone` resources.
    """
    resource_class = Zone

    def list(self, zone_name=None):
        """
        Get a list of all zones if zone_name is None.
        Or association table zone_name/node_id if zone_name has been defined.

        :rtype: List of zones
        """
        if zone_name is not None:
            zone_list = self._list("/zones/list?zone_name=%s" % zone_name, "zones")
        else:
            zone_list = self._list("/zones/list", "zones")
        print('List of zones')
        print(zone_list)
        return zone_list

    def add(self, zone_name, node_id=None):
        """
        If node_id is None then create new zone with zone_name
        else create association zone_name/node_id

        :rtype: List of zones
        """

        #body = {"network": kwargs}
        #return self._create('/os-networks', body, 'network')

        #return self._update("/os-aggregates/%s" % base.getid(aggregate), body, "aggregate")
        if node_id is not None:
            zone_list = self._list("/zones/add?zone_name=%s&node_id=%s" % (zone_name, node_id), "zones")
        else:
            zone_list = self._list("/zones/add?zone_name=%s" % zone_name, "zones")
        print('Add zone')
        print(zone_list)
        return zone_list

    def delete(self, zone_name, node_id=None):
        """
        If node_id is None then delete zone and all associations
        else delete association zone_name/node_id

        :rtype: List of zones
        """
        #self._delete("/os-zones/%s" % base.getid(network))
        if node_id is not None:
            zone_list = self._list("/zones/delete?zone_name=%s&node_id=%s" % (zone_name, node_id), "zones")
        else:
            zone_list = self._list("/zones/delete?zone_name=%s" % zone_name, "zones")
        print('Delete zone')
        print(zone_list)
        return zone_list

